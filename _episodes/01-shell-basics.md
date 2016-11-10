---
title: "Command line/shell"
teaching: 55
exercises: TODO
questions:
- "Why and how using command line shell efficiently could increase reproducibility of neuroimaging studies?"
- "How we could help assuring that our scripts *do the right thing*?"
objectives:
- "Explain basic differences among available shells and their use in
  neuroimaging toolkits"
- "Using shell as a working medium explain the role of some most important environment variables"
- "Provide hints on efficient use of the collected shell history of commands"
- "Explain how to make shell scripts more robust and less dangerous"
- "Introduce basics of unit-testing"
- "Write basic unit-test for shell commands"
keypoints:
- Command line shell is a powerful tool, and learning additional
  "hints" could help to make its use much more efficient, less
  error-prone, and thus more reproducible
- "Environment variables play a big role in defining scripts behavior"
- You can largely avoid manual retyping of previous commands and their
  options
- "Shell scripts are powerful but by default could cause big pain"
---

- For windows users:  how to get a shell...

   - best practice: upgrading to Windows 10 to get a unix shell?



## What is a “shell”?

*Shell* commonly refers to UNIX shell environment, which in its core
function provides users with a CLI (command line interface) to
manipulate "environment variables", to execute external commands, and
to script (program) sets of those commands to be (re-)executed
repetitively or conditionally (e.g., provides constructs for loops,
functions, conditions).  Because manipulation of files is one of the
main tasks to be accomplished in a shell, usually shell either comes
with common commands (such as `cp`, `mv`, etc.) built-in or
accompanied by an additional package (e.g., `coreutils` in Debian)
providing those.

- Tale of Yarik & Perl

Unlike GUI integrated environments with lots of functionality exposed
in menu items and icons, shell is truly a "black box", which has a
lot of powerful features which you need to discover first to be able
to use it efficiently.

In this part we will first get familiarized with basic (and possibly
advanced) features of a shell and shell scripting, and then review
aspects which particularly relate to reproducibility, as a principle
of having a good control over execution of commands -- knowing which
command actually was ran, inspecting available history of the
commands, and verifying that a script did not complete while hiding
failed interim execution.

- Why shell:
- repeatability
- there are different shells
- existing software toolkits already use various shells and it is
  important to at least be aware of the difference...

> ## External teaching materials
>
> Before going through XXX
>
>   - [Software Carpentry: The Unix Shell (full: 1 h 35 min, familiarize: 10 min)](http://swcarpentry.github.io/shell-novice/)
{: .callout}

> ## Additional materials
>
>   - [Wikipedia:Unix shell](https://en.wikipedia.org/wiki/Unix_shell)
>   - [Wikipedia:Comparison of command shells](https://en.wikipedia.org/wiki/Comparison_of_command_shells)
>
> Relevant Books:
>
>   - [Data Science at the command line](http://datascienceatthecommandline.com) which also contains a list of
>     command line tools from useful for “data science”
{: .callout}


## Commonly used shells and relation to existing neuroimaging projects

> ## How can you determine what shell are you currently in?
> ~~~
> $ echo $SHELL
> ~~~
> {: .bash}
{: .challenge}

> ## What is a shebang?
{: .challenge}

> ## Could a shebang carry options?
>
> TODO
{: .challenge}


- **sh** - a POSIX compliant shell. Generic name, not a specific project
  - Most portable (since standard)
  - Many FSL scripts (claim to be)
- **ksh** - KornShell.  Based on older bash, but also became a root for tcsh, zsh and others
- **dash** - an implementation of a POSIX compliant shell (**sh**)
  - You will not see it used directly in a shebang
- **bash** - Bourne Again SHell.
  - (Optionally) sh-compliant but with additional features from
    **ksh** and **csh**
  - Next most portable and most popular for shell scripting (after **sh**)
- **csh/tcsh** - shell which aimed to provide interface similar to C programming language.
  - Heavily used by FreeSurfer, AFNI (primarily @ scripts)
- **zsh** - Powerful, but not POSIX/bash-compatible. Inspired by many features from ksh and tcsh.
  - Rarely used for generic scripting

> ## References
> Additional materials
> - [Wikipedia:Comparison of command shells](https://en.wikipedia.org/wiki/Comparison_of_command_shells)
{: .callout}

> ## How to check if a given script conforms to POSIX standard and carries no "bashisms"?
>
>  TODO
{: .challenge}


## Environment variables

Environment variables are not a feature of `a shell` per se. Every
process on any operating system inherits some "environment variables"
from its parent process.  shell just streamlines manipulation of those
environments and also uses some of them directly to guide its own
operation.  Let's overview most commonly used and manipulated
environment variables, which are important to be aware of if you want
to be sure that you are using external commands and libraries you
think you are using.

### PATH - determines full path to the command to be executed

Whenever a command specified without providing a full path on a
filesystem to it, PATH environment variable is the one consulted to
the paths where to look for the command.  You might have multiple
implementations or versions of the same command available at different
locations, which might be specified within PATH variable (separated
with a colon).  Although a very simple concept, it is a power-horse
for "overlay distributions" (such as [conda]), or "overlay
environments (such as [virtualenv] in Python, or [modules]), and also
the source of a confusion in many cases where some not intended
command is ran instead.  So, any tool which aims to capture
state of the computational environment for later re-execution, might
need to store the value of the PATH variable to guarantee that even
given the same set of files, the same commands are executed.

> ## How to determine full path to the command I am about to use?
>
> ~~~
> $ which EXEC
> ~~~
> {: .bash}
{: .callout}


> ## Beware of built-in commands
>
> Some commands might be implemented by shell itself, and their
> implementation might differ from the one provided by some core
> set of tools.
>
> Note that `which` is not a built-in command in bash (but is in
> zsh), so in bash you would not be able to "resolve" built-in
> commands such as e.g. `pwd`.
>
> ~~~
> $ pwd -h           # bash built-in
> bash: pwd: -h: invalid option
> pwd: usage: pwd [-LP]
>
> $ which pwd
> /bin/pwd
>
> $ /bin/pwd -h      # provided by coreutils
> /bin/pwd: invalid option -- 'h'
> Try '/bin/pwd --help' for more information.
> ~~~
> {: .bash}
{: .callout}


### LD_LIBRARY_PATH - determine which dynamic library is used

To improve maintainability, and to make distribution smaller, most
often commands we use rely on dynamic linking to reuse common
functionality provided by shared dynamic libraries.  Particular list
of dynamic libraries which executable needs is often stored also
without full paths, so `ld.so` (`/lib/ld-linux.so.2` e.g. on recent
Debian systems) which takes care about executing those binaries needs
to determine which particular libraries to load.  Similarly to how
`PATH` variable determines resolution paths for execution of commands,
`LD_LIBRARY_PATH` environment variable provides resolution paths for
loading dynamic libraries.  Unlike `PATH`, `ld.so` does assume a list
of default paths (e.g., `/lib`, then `/usr/lib` on Linux systems), so
in your environment you might not even have it set explicitly.

> ## How to discover which library is used:
>
> ldd EXEC or ldd LIBRARY
{: .callout}


> ## Swiss knife to inspect execution on Linux systems
>
> strace traces "system calls" -- calls your program makes to the
> core of the operating system (i.e., kernel)
>
> strace -e open EXEC
{: .callout}


> ## Possible conflicts
>
> It might happen that `PATH` would point to one environment first,
> while LD_LIBRARY_PATH point to libraries from another environment.
> which could cause either incorrect or hard to diagnose later
> behavior.  In general you should avoid manipulating those two
> variables manually.
{: .callout}

### PYTHONPATH - determine which Python module to be used

The idea of controlling resolution paths via environment variables
expands further into language specific domains.  E.g., Python consults
`PYTHONPATH` variable to possibly change the search paths for Python
modules.

> ## Possible side-effect
>
> Using a mix of system-wide , per-user installed
> app/module while having additional custom installations in
>
> python -c 'import sys; print sys.path'
>
>
{: .callout}

Exercise: Beware of e.g. ~/.local/lib/python2.7/site-packages (could use strace to figure out)

### Additional aspects

> Exported or "local" variables
>
> Some variables are "exported" so they will be inherited by any new
> process you would start in a shell.  Some are local, and will not be
> inherited.
>
> 1. How could you determine if variable is exported or not?
> 2. Get a list of all local environments (present in your shell but
>    not exported)
>
{: .challenge}



## Configuration files for login and non-login shells

## Efficient use of the interactive shell

### aliases

### Editing command line

Two modes are usually supported -- `emacs` and `vim` .

**set -o emacs** to enter emacs mode (default), **set -o vi** to enter
vi mode.  Further discussion and examples are for the default,
**emacs** mode.

Ctrl-x Ctrl-e (in emacs bash), (could be Meta-e in zsh) -- edit
cmdline in the editor (as defined by `VISUAL` environment variable)

## set -o

Shells provide a set of configurable options which could be enabled or
disabled using `set` command.  Use `set -o` to print current settings
you have in your shell

## Using/leaving breadcrumbs

### Completions

### Shell history

- exploring the history
- keeping shell history forever (e.g. http://www.onerussian.com/Linux/bash_history.phtml ).  Your own “lab book” if you work in shell lots of time.
- quickly searching through previous history entries
- re-using arguments from previously executed commands in current command


> ## Exercises and challenges (click on the arrow to the right to open)
>
>  Boxes with "challenges" can be interleaved with the lesson materials.
>  Consider adding a challenge every 15 minutes or so.
>    - This helps participants stay engaged.
>    - It surfaces questions that learners have as they go along.
>    - It breaks up the instruction, providing a bit of a diversion.
>    - It gives people a chance to engage in peer instruction, which is
>      is [known to help learning](https://en.wikipedia.org/wiki/Peer_instruction).
{: .challenge}

### Creating log files

- >

`set -o noclobber` is recommended to forbid overwriting previously
existing files.  `>|` could be used to explicitly instruct overwriting
already existing file

- `|&` (bash only) == `2>&1 |`

(3dLME -help) `tcsh -x LME.txt |& tee diary.txt &   (|& -- bash)

- tee

## Hints for correct/robust scripting in shell

### Fail early, behave deterministically

set -eu

POSIX defines some commands as "special", which would cause entire
script to exit (even without set -e) if they return non-0 value (
break : . continue eval exec exit export readonly return set
shift trap unset).
https://www.gnu.org/software/bash/manual/html_node/Special-Builtins.html#Special-Builtins

, ${var:-DEFAULT},  etc


How to check for bashisms in case of using regular sh (#!/bin/sh)?

### (Unit)testing

(bats, shunit)

