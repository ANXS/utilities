## Ansibles - utilities [![Build Status](https://travis-ci.org/Ansibles/utilities.png)](https://travis-ci.org/Ansibles/utilities)

Ansible role that installs a selection of useful, must-have utilities. Additional ones can be adding them to the `utilities_extras` list.

##### The list of basic utilities includes:
- **ack**: grep, optimized for programmers
- **command-not-found**: suggest installation of packages in interactive bash sessions
- **curl**: command line tool for transferring data with URL syntax
- **dmidecode**: reports information about your system's hardware as described in your system BIOS according to the SMBIOS/DMI standard
- **htop**: interactive process viewer for Linux
- **iftop**: display bandwidth usage on an interface
- **iotop**: display io usage on behalf of which process on an interface
- **nmap**: Security Scanner For Network Exploration & Hacking
- **mosh**: mobile shell
- **pciutils**: collection of programs for inspecting and manipulating configuration of PCI devices
- **sysstat**: utility comprised of several tools that offers advanced system performance monitoring
- **tmux**: terminal multiplexer
- **tshark**: dump and analyze network traffic

##### Distribution specific utilities:

###### Debian/Ubuntu/...:
- **acl**: much more flexible way of specifying permissions on a file or other object than the standard Unix
- **apticron**: Get email notifications for updates (needs configuration)
- **debconf**: utility for performing system-wide configuration tasks on Unix-like operating systems
- **update-notifier-common**: no explanation needed...

#### Requirements & Dependencies
- Tested on Ansible 1.4 or higher


#### Variables

```yaml
utilities_extras: []            # List of additional utility package names to be installed
```


#### License

Licensed under the MIT License. See the LICENSE file for details.


#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/ansibles/utilities/issues)!
