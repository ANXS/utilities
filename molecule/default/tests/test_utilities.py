"""Testinfra tests for anxs-utilities role."""


BASE_PACKAGES = [
    "curl",
    "htop",
    "tmux",
    "tree",
    "mtr",
    "nmap",
    "socat",
    "pv",
    "ncdu",
    "whois",
]

DEBIAN_FAMILY_EXTRAS = ["acl", "debconf"]

EXTRAS_FROM_CONVERGE = ["jq"]


def test_base_packages_installed(host):
    """Every target installs the core base utilities."""
    for pkg in BASE_PACKAGES:
        assert host.package(pkg).is_installed, f"{pkg} should be installed"


def test_debian_family_extras_installed(host):
    """Debian family gets acl and debconf via utilities_distribution_debian."""
    os_family = host.ansible("setup")["ansible_facts"]["ansible_os_family"]
    if os_family != "Debian":
        return
    for pkg in DEBIAN_FAMILY_EXTRAS:
        assert host.package(pkg).is_installed, f"{pkg} should be installed on Debian family"


def test_extras_installed(host):
    """utilities_extras from converge.yml should be honored."""
    for pkg in EXTRAS_FROM_CONVERGE:
        assert host.package(pkg).is_installed, f"extras package {pkg} should be installed"


def test_netcat_rename_ubuntu(host):
    """Ubuntu renames netcat to netcat-openbsd."""
    facts = host.ansible("setup")["ansible_facts"]
    if facts["ansible_distribution"] != "Ubuntu":
        return
    assert host.package("netcat-openbsd").is_installed
    assert not host.package("netcat").is_installed


def test_netcat_rename_debian13(host):
    """Debian 13 renames netcat to netcat-openbsd."""
    facts = host.ansible("setup")["ansible_facts"]
    if facts["ansible_distribution"] != "Debian":
        return
    if int(facts["ansible_distribution_major_version"]) < 13:
        return
    assert host.package("netcat-openbsd").is_installed


def test_dropped_packages_not_installed(host):
    """pstack and ltrace were dropped from the baseline when modern Debian
    stopped carrying them. Confirm nothing brings them back."""
    assert not host.package("pstack").is_installed
    assert not host.package("ltrace").is_installed
