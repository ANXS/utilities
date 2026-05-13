## [ANXS](https://github.com/ANXS) - utilities

[![CI Status](https://img.shields.io/github/actions/workflow/status/anxs/utilities/ci.yml)](https://github.com/ANXS/utilities/actions/workflows/ci.yml)
[![Maintenance](https://img.shields.io/maintenance/yes/2026.svg)](https://github.com/ANXS/utilities)
[![Ansible Role](https://img.shields.io/ansible/role/d/anxs/utilities)](https://galaxy.ansible.com/ui/standalone/roles/ANXS/utilities/)
[![License](https://img.shields.io/github/license/ANXS/utilities)](https://github.com/ANXS/utilities/blob/master/LICENSE)

Ansible role that installs a curated set of command-line utilities (curl, htop, tmux, tree, mtr, nmap, and friends) with per-distribution excludes and package renames.

## Requirements & Dependencies

* Ansible 2.13 or higher.
* Ubuntu 20.04+ or Debian 12+.

## Variables

Some commonly adjusted variables. See [`defaults/main.yml`](https://github.com/ANXS/utilities/blob/master/defaults/main.yml) for the full set.

* `utilities_base` is the default list of utilities installed on every host.
* `utilities_extras` (default `[]`) appends custom packages without replacing the base list.
* `utilities_exclude` drops packages from the base list before install.
* `utilities_renames` maps a base package name to a per-distro alternative (e.g. `netcat: netcat-openbsd`). Set in `vars/<distro>-<version>.yml`.
* `utilities_distribution_debian` adds Debian-family-only packages (e.g. `acl`, `debconf`).
* `utilities_distribution_exclude` removes packages at install time (e.g. `pstack`, `ltrace` on Debian 13 where they're no longer available).

## Testing

Tests use [Molecule](https://github.com/ansible/molecule) with Docker and [Testinfra](https://testinfra.readthedocs.io/). Run the full suite with `make test`, or target a specific platform (e.g. `make test-debian13`).

The test suite verifies base utilities installed everywhere, Debian-family extras (acl, debconf), honored `utilities_extras`, per-distro package renames (`netcat` → `netcat-openbsd` on Ubuntu and Debian 13), and per-distro excludes (`pstack`, `ltrace` absent on Debian 13). Tests run across Ubuntu 20.04/22.04/24.04 and Debian 12/13.

## Note on AI Usage

This project has been developed with AI assistance. Contributions making use of AI generated content are welcome, however they _must_ be human reviewed prior to submission as pull requests, or issues. All contributors must be able to fully explain and defend any AI generated code, documentation, issues, or tests they submit. Contributions making use of AI must have this explicitly declared in the pull request or issue. This also applies to utilization of AI for reviewing of pull requests.

## Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/ANXS/utilities/issues)!
