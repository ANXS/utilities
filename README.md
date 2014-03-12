## Ansibles - utilities [![Build Status](https://travis-ci.org/Ansibles/utilities.png)](https://travis-ci.org/Ansibles/utilities)

Ansible role that installs a selection of useful, must-have utilities. Additional ones can be adding them to the `utilities_extras` list.

The basic install includes:
- command-not-found
- curl
- debconf
- dmidecode
- htop
- iftop
- iotop
- nmap
- mosh
- pciutils
- sysstat
- tmux
- tshark

#### Requirements & Dependencies
- Tested on Ansible 1.3 or higher

#### Variables

```yaml
utilities_extras: []            # List of additional utility package names to be installed
```

#### License

Licensed under the MIT License. See the LICENSE file for details.

#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/ansibles/utilities/issues)!
