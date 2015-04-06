## ANXS - utilities [![Build Status](https://travis-ci.org/ANXS/utilities.png)](https://travis-ci.org/ANXS/utilities)

Ansible role that installs a selection of useful, must-have utilities. Additional ones can be adding them to the `utilities_extras` list.

##### The list of basic utilities includes:
- **ack**: grep, optimized for programmers
- **command-not-found**: suggest installation of packages in interactive bash sessions
- **curl**: command line tool for transferring data with URL syntax
- **dstat**: tool for generating system resource statistics
- **dmidecode**: reports information about your system's hardware as described in your system BIOS according to the SMBIOS/DMI standard
- **ethtool**: display or change ethernet card settings
- **htop**: interactive process viewer for Linux
- **iftop**: display bandwidth usage on an interface
- **iotop**: display io usage on behalf of which process on an interface
- **iperf**: TCP/UDP bandwidth measurement tool
- **lsof**: list open files
- **ltrace**: library call tracer
- **nmap**: Security Scanner For Network Exploration & Hacking
- **mosh**: mobile shell
- **multitail**: interactively tail multiple files
- **mtr**: a network diagnostic tool
- **ncdu**: interactive console disk usage visualizer
- **netcat**: reads and writes data across network
- **pciutils**: collection of programs for inspecting and manipulating configuration of PCI devices
- **pstack**: attaches to the active processes named by the pids on the command line , and prints out an execution stack trace
- **pv**: see the progress of data through a pipeline
- **smem**: provides numerous reports on memory usage
- **socat**: establishes two bidirectional byte streams and transfers data between them
- **strace**: trace system calls and signals
- **sysstat**: utility comprised of several tools that offers advanced system performance monitoring
- **tmux**: terminal multiplexer
- **tree**: recursive directory listing program
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


#### Testing
This project comes with a VagrantFile, this is a fast and easy way to test changes to the role, fire it up with `vagrant up`

See [vagrant docs](https://docs.vagrantup.com/v2/) for getting setup with vagrant


#### License

Licensed under the MIT License. See the LICENSE file for details.


#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/ANXS/utilities/issues)!
