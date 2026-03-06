## Overview
A small data cleaning experiment.

Blogged about it [here](https://jelaiw.github.io/blog/2026/03/01/quotes-data.html).

## Demo
Install `fortune` via package manager.

Below steps are from a GitHub Codespaces devcontainer (default image), but should be more or less the same anywhere you can grab and install it from a package.

```sh
$ sudo apt update
Get:1 http://archive.ubuntu.com/ubuntu noble InRelease [256 kB]
Get:2 http://archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                                                                                                        
Get:3 http://archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]                                                                                                      
Get:4 https://dl.yarnpkg.com/debian stable InRelease                                                                                                                           
Get:5 https://repo.anaconda.com/pkgs/misc/debrepo/conda stable InRelease [3961 B]                                                                      
Get:6 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]                                                        
Get:7 http://archive.ubuntu.com/ubuntu noble/restricted amd64 Packages [117 kB]
Get:8 http://archive.ubuntu.com/ubuntu noble/main amd64 Packages [1808 kB]                            
Get:9 http://archive.ubuntu.com/ubuntu noble/universe amd64 Packages [19.3 MB]
--- SNIP ---

$ sudo apt install fortune-mod
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  fortunes-min librecode0
Suggested packages:
  fortunes x11-utils bsdmainutils
The following NEW packages will be installed:
  fortune-mod fortunes-min librecode0
0 upgraded, 3 newly installed, 0 to remove and 131 not upgraded.
Need to get 711 kB of archives.
After this operation, 2129 kB of additional disk space will be used.
Do you want to continue? [Y/n] 
Get:1 http://archive.ubuntu.com/ubuntu noble/main amd64 librecode0 amd64 3.6-26 [625 kB]
Get:2 http://archive.ubuntu.com/ubuntu noble/universe amd64 fortune-mod amd64 1:1.99.1-7.3build1 [32.7 kB]
Get:3 http://archive.ubuntu.com/ubuntu noble/universe amd64 fortunes-min all 1:1.99.1-7.3build1 [53.1 kB]
Fetched 711 kB in 1s (796 kB/s)        
Selecting previously unselected package librecode0:amd64.
(Reading database ... 58629 files and directories currently installed.)
Preparing to unpack .../librecode0_3.6-26_amd64.deb ...
Unpacking librecode0:amd64 (3.6-26) ...
Selecting previously unselected package fortune-mod.
Preparing to unpack .../fortune-mod_1%3a1.99.1-7.3build1_amd64.deb ...
Unpacking fortune-mod (1:1.99.1-7.3build1) ...
Selecting previously unselected package fortunes-min.
Preparing to unpack .../fortunes-min_1%3a1.99.1-7.3build1_all.deb ...
Unpacking fortunes-min (1:1.99.1-7.3build1) ...
Setting up librecode0:amd64 (3.6-26) ...
Setting up fortunes-min (1:1.99.1-7.3build1) ...
Setting up fortune-mod (1:1.99.1-7.3build1) ...
Processing triggers for man-db (2.12.0-4build2) ...
Processing triggers for libc-bin (2.39-0ubuntu8.6) ...
--- SNIP ---

$ cd /usr/share/games/fortunes/
$ ls
fortunes  fortunes.dat  fortunes.u8  literature  literature.dat  literature.u8  riddles  riddles.dat  riddles.u8
$ cp /workspaces/favorite-quotes/fortune/quotes .
cp: cannot create regular file './quotes': Permission denied
$ sudo cp /workspaces/favorite-quotes/fortune/quotes .
$ sudo strfile quotes 
"quotes.dat" created
There were 123 strings
Longest string: 707 bytes
Shortest string: 21 bytes
$
```
Quick test.

```
$ fortune quotes
bash: fortune: command not found
$ export PATH=$PATH:/usr/games
$ fortune quotes
I don't wait for moods. You accomplish nothing if you do that. Your mind must know it has got to get down to work.
- Pearl Buck
$ fortune quotes
Work is of two kinds: first, altering the position of matter at or near the Earth's surface relative to other matter; second, telling other people to do so.
- Bertrand Russell
$ fortune quotes
They must find it hard to take Truth for authority who have so long mistaken Authority for Truth.
A Retort, from Gerald Massey's Lectures c.1900; often cited as They must find it difficult, those who have taken authority as truth, rather than truth as authority.
$ fortune quotes
A rich person should leave his kids enough to do something, but not enough to do nothing.
- Warren Buffett
$ fortune quotes
Today is your day! Your mountain is waiting. So ... get on your way.
- Theodore Seuss Geisel (Dr. Seuss)
$
```

Left the fiddly bits in.
