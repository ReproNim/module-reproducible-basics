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

## What is a “shell”?
- Just two words on its purpose
- Tale of Yarik & Perl


> ## References
> Online courses:
> - [Software Carpentry: The Unix Shell (full: 1 h 35 min, familiarize: 10 min)](http://swcarpentry.github.io/shell-novice/)
>
> Additional materials:
> - [Wikipedia:Unix shell](https://en.wikipedia.org/wiki/Unix_shell)
> - [Wikipedia:Comparison of command shells](https://en.wikipedia.org/wiki/Comparison_of_command_shells)
>
> Relevant Books:
> - [Data Science at the command line](http://datascienceatthecommandline.com) which also contains a list of
>   command line tools from useful for “data science”
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

> ## Could shebang carry options?
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
>  TODO: move into scripting section
{: .challenge}


## Most important environment variables

Environment variables and how that relates to conda, virtualenv, modules.  How does it relate to capturing information about what environment you worked in while you did analysis 
Important variables:
generic:  PATH, LD_LIBRARY_PATH
How to discover their effect:
which EXEC
ldd EXEC or ldd LIBRARY
strace -e open EXEC
Possible conflicts
PATH selects one env first, LD_LIBRARY_PATH points to libraries from another env
Python: PYTHONPATH
Possible side-effects: using system-wide installed app/module while having additional custom installations in
python -c 'import sys; print sys.path'
Exercise: Beware of e.g. ~/.local/lib/python2.7/site-packages (could use strace to figure out)

## Configuration files for login and non-login shells

## Efficient use of the interactive shell

### aliases

### Editing command line

Two modes are usually supported -- emacs and vim

**set -o emacs** to enter emacs mode (default), **set -o vi** to enter
vi mode.  Further discussion and examples are for the default,
**emacs** mode.

Ctrl-x Ctrl-e (in emacs bash), (could be Meta-e in zsh) -- edit
cmdline in the editor (as defined by `VISUAL` environment variable)

### History

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


## Shell scripting

> ## References
> Online courses:
> - [Software Carpentry: The Unix Shell (section "Shell Scripts" 15 min)](http://swcarpentry.github.io/shell-novice/06-script/)
{: .callout}

## Hints for correct/robust scripting in shell

### Fail early, behave deterministically

set -eu , ${var:-DEFAULT},  etc

How to check for bashisms in case of using regular sh (#!/bin/sh)?

### (Unit)testing

(bats, shunit)

