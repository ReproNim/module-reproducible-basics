---
title: "Command line/shell"
teaching: 150
exercises: 30
questions:
- "Why and how does using the command line/shell efficiently increase reproducibility of neuroimaging studies?"
- "How can we assure that our scripts *do the right thing*?"
objectives:
- "Understand basic differences among available shells and their use in
 neuroimaging toolkits"
- "Using a shell as a working medium"
- "Explain the role of some of the most important environment variables"
- "Provide hints on efficient use of the collected shell history of commands"
- "Explain how to make shell scripts more robust and less dangerous"
- "Introduce basics of runtime and unit testing"
keypoints:
- "There are a number of incompatible shells. Different
  neuroimaging tools may use specific shells and thus provide
  instructions that are not compatible with your current shell."
- "A command line shell is a powerful tool and learning additional
 'tricks' could help to make its use much more efficient, less
 error-prone, and thus more reproducible."
- "Shell scripting is the most accessible tool to automate execution of
  arbitrary set of commands. This avoids manual retyping of the
  same commands and in turn will avoid typos and erroneous analyses."
- "Environment variables play a big role in defining script behavior."
- "You can automate testing of the execution of your commands to
  provide at least some verifiable guarantee of correct execution
  across different systems."
- "Shell scripts are powerful but if misused can cause big problems."
---

> ## You can skip this lesson if you can answer these questions: &nbsp; &#8680;
>
>  - What factors affect execution of a given typed command in shell?
>  - How can you script the execution of a list of commands given user input
>    arguments?
>  - How can you guarantee that your script was executed correctly and will not
>    fail during execution?
>  - How can you use text editors to edit your current command line?
>  - How can you quickly recover sequence of commands you have ran in shell
>    (e.g. a year ago while performing some analysis)?
{: .challenge}


- For Windows OS users: If you do not have remote or virtual
  environment with Unix or Linux system, you can
  [enable "native" Linux bash shell on your Windows 10 system](http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/).



## What is a “shell”?

*Shell* commonly refers to the UNIX shell environment, which in its
core function provides users with a CLI (command line interface) to
manipulate "environment variables" and to execute external
commands. Because desired actions are expressed as typed commands it
becomes possible to script (program) sets of those commands to be
(re-)executed repetitively or conditionally (e.g., provides constructs
for loops, functions, conditions).  So, in contrast to GUI (graphical
user interface), such automation via scripting is a native feature of
a CLI shell.  Unlike GUI integrated environments with lots of
functionality exposed in menu items and icons, shell is truly a "black
box", which has a lot of powerful features which you need to discover
first to be able to use it efficiently.  Because manipulation of files
is one of the main tasks to accomplish in a shell, usually a shell
either comes with common commands (such as `cp`, `mv`, etc.) built-in
or is accompanied by an additional package (e.g., `coreutils` in
Debian) providing those helpful command line utilities.

In this module we will first become familiarized with basic (and
possibly advanced) features of a shell and shell scripting, and then
review a few aspects that particularly relate to reproducibility, as
a principle of having good control over commands execution -- knowing
which command actually was ran, what conditions could have potentially
affected their execution, inspecting available history of the
commands, and verifying that a script did not complete while hiding
failed interim execution.

> ## External teaching materials
>
> Before going through the rest of this lesson, you should learn
> basics of shell usage and scripting. Following lesson provides a
> good overview of all basics concepts.  Even if you are familiar with
> shell and shell scripting, please review materials of the lesson and
> try to complete all exercises in it, especially if you do not know
> correct answer to them right away:
>
>   - [Software Carpentry: The Unix Shell (full: 1 h 35 min, review: 20 min)](http://swcarpentry.github.io/shell-novice/)
{: .callout}

> ## Additional materials
>
> If you are interested to know more about history and features of
> various shells, please review materials under following external links:
>
>  - ["Teaching Notes" of the above "The Unix Shell" lesson](https://swcarpentry.github.io/shell-novice/guide/)
>    provides a number of hints and links to interesting related resources
>  - [Wikipedia:Unix shell](https://en.wikipedia.org/wiki/Unix_shell)
>
> Relevant Books:
>
>  - [Data Science at the Command Line](http://datascienceatthecommandline.com), which also contains a list of
>   command line tools from useful for “data science”
{: .callout}

## Challenges

> ## How can you determine what shell are you currently in?
> ~~~
> % echo $SHELL
> ~~~
> {: .bash}
{: .solution}

> ## How do you change the login shell for your account?
> ~~~
> % chsh
> ~~~
> {: .bash}
{: .solution}

> ## What is a shebang?
> It is the first line in the script, and which starts with `#!` 
> followed by the command to be used to interpret the script, e.g.
> if a file `blah` begins with the following:
> ~~~
> #!/bin/bash
> echo "Running this script using bash"
> ~~~
> {: .bash}
> then running `./blah` is analogous to calling `/bin/bash ./blah` .
> The string "#!" is read out loud 
> as "hash-bang" and therefore is shortened to "shebang."
{: .solution}


> ## Could a shebang carry options?
>
> To help answering the question answer which of the following shebangs would be correct and what would be
> their effect
>
> 1. `#!/bin/bash`
> 2. `#!/bin/bash -e`
> 3. `#!/bin/bash -ex`
> 4. `#!/bin/bash -e -x`
>
> > ## Answer
> > Shebang can carry up to 1 option, so 1-3 are correct.
> {: .solution}
{: .challenge}


## Commonly used shells and relation to existing neuroimaging projects


- **sh** - a POSIX compliant shell. Generic name, not a specific project
   - Most portable (since standard)
   - Many FSL scripts (attempt to be)
- **ksh** - KornSHell. Based on older bash, but also became a root for tcsh, zsh and others
- **dash** - an implementation of a POSIX compliant shell (**sh**)
   - You will not see it used directly in a shebang
- **bash** - Bourne Again SHell.
   - (Optionally) sh-compliant but with additional features from **ksh** and **csh**
   - Next most portable and most popular for shell scripting (after
     **sh**) and generally available (in contrast to **zsh**)
- **csh/tcsh** - shell which aimed to provide interface similar to C programming language.
   - Heavily used by FreeSurfer, AFNI (primarily @ scripts)
- **zsh** - Powerful, but not POSIX/bash-compatible. Inspired by many features from **ksh** and **tcsh**.
   - Rarely used for generic scripting

> ## References
> Additional materials
> - [Wikipedia:Comparison of command shells](https://en.wikipedia.org/wiki/Comparison_of_command_shells)
{: .callout}

> ## How do you change current shell in your session?
> You just start it. E.g.
> ~~~
> % tcsh
> ~> 
> ~~~
> {: .bash}
> would enter a new `tcsh` session.  You can exit it and return to
> your previous shell by typing `exit` or just pressing `Ctrl-d`.
{: .solution}



## Environment variables

Environment variables are not a feature of `a shell` per se. Every
process on any operating system inherits some "environment variables"
from its parent process. A shell just streamlines manipulation of those
environments and also uses some of them directly to guide its own
operation. Let's overview the most commonly used and manipulated
environment variables. These variables are important because they
impact what external commands and libraries you are using.

### PATH - determines full path to the command to be executed

Whenever running a command without providing its full path on the
filesystem, the `PATH` environment variable is consulted to determine
which paths to look for the command. You might have multiple
implementations or versions of the same command available at different
locations, which might be specified within the PATH variable (separated
with a colon). Although a very simple concept, it is a workhorse
for "overlay distributions" (such as [conda](https://conda.io)), or "overlay
environments (such as [virtualenv](https://virtualenv.pypa.io) in
Python, or [modules](http://modules.sourceforge.net/) often used on
HPC), and it is also
the source of confusion in many cases where some unintended
command is run instead. That is why any tool which aims to capture the
state of the computational environment for later re-execution might
need to store the value of the PATH variable to guarantee that even
given the same set of files, the same commands are executed. For example,
we may have two different versions of AFNI installed in different locations;
without specifying the path to a particular installation of AFNI, we may
unintentionally run a different version and end up with different results.

> ## How can you determine full path to the command that you are about to use?
>
> To see which command will actually be run when you intend to run a
> `COMMAND`, use `which` helper, e.g.
> ~~~
> $ which afni
> /usr/bin/afni
> ~~~
> {: .bash}
{: .solution}


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
> % pwd -h      # bash built-in
> bash: pwd: -h: invalid option
> pwd: usage: pwd [-LP]
>
> % which pwd
> /bin/pwd
>
> % /bin/pwd -h   # provided by coreutils
> /bin/pwd: invalid option -- 'h'
> Try '/bin/pwd --help' for more information.
> ~~~
> {: .bash}
{: .callout}


> ## How can you add a new path for shell to look for commands in?
>
> 1. So that those commands take precedence over other commands named
> the same way but available elsewhere on the `PATH`?
>
> 2. So those commands are ran only if not found elsewhere on the
> on the `PATH`? (rarely needed/used case)
>
> > ## Solution
> > For a new path /a/b/c:
> > 1. Use  PATH=/a/b/c:$PATH
> > 2. Use  PATH=$PATH:/a/b/c
> {: .solution}
{: .challenge}

> ## How can you determine environment variables of a process?
>
> Since each process inherits and possibly changes environment
> variables so that its child processes inherit them in turn, it is
> often important to be able to introspect them.  So given a `PID` of
> a currently running process (e.g., `$$` variable in POSIX shell contains
>`PID` of your active shell), how can you determine its environment variables?
>
> > ## Solution
> > 1. By looking into `/proc/PID/environ` file on Unix/Linux
> > systems.  Exercise:  entries in that file separated with byte
> > `0`. Use `tr` command to make them separated by a new line.
> > 2. `ps e PID` will list all environment variables with their
> > values
> > 3. `e` shortcut in `htop` will show environment variables of the
> > selected process
> {: .solution}
{: .challenge}

> ## Why is ${variable} is preferable over $variable?
>
> You use ${variable} to safely concatenate a variable with another string.  
> For instance if you
> have a variable `filename` that contains value `preciousfile`
> `$filename_modified` will refer to the value of possibly undefined
> `filename_modified` variable, whenever `${filename}_modified` would
> produce desired value of `preciousfile_modified`
{: .solution}



### LD_LIBRARY_PATH - determine which dynamic library is used

To improve maintainability and to make distributions smaller, most
programs use dynamic linking to reuse common
functionality provided by shared libraries. The particular
list of dynamic libraries which an executable needs is often stored
also without full paths, so `ld.so` (e.g. `/lib/ld-linux.so.2` on
recent Debian systems), which takes care of executing those binaries,
needs to determine which particular libraries to load. Similar to
how `PATH` variable determines resolution paths for execution of
commands, the `LD_LIBRARY_PATH` environment variable provides resolution
paths for loading dynamic libraries. Unlike `PATH`, `ld.so` does
assume a list of default paths (e.g., `/lib`, then `/usr/lib` on Linux
systems, as defined in `/etc/ld.so.conf` file(s)), so in your
environment you may not have even set it explicitly.

> ## How can you discover which library is used?
>
> `ldd EXEC` or `ldd LIBRARY` would list libraries a given binary or a
> library is linked against and provide a full path, if it finds them
> using `ld`'s default paths, or `LD_LIBRARY_PATH` variable. E.g.
> ~~~
> % ldd /usr/lib/afni/bin/afni | head
>	linux-vdso.so.1 (0x00007fffd41ca000)
>	libXm.so.4 => /usr/lib/x86_64-linux-gnu/libXm.so.4 (0x00007fd9b2075000)
>	libmri.so => /usr/lib/afni/lib/libmri.so (0x00007fd9b1410000)
>   ...
> ~~~
> {: .bash}
{: .callout}


> ## Swiss army knife to inspect execution on Linux systems
>
> [strace](https://en.wikipedia.org/wiki/Strace) traces "system calls"
> -- calls your program makes to the core of the operating system (i.e., kernel).
> This way you can discover what files any given program tries to
> access or open for writing, which other commands it tries to run
> etc.  Try running  `strace -e open` and provide some command to be
> executed.
>
{: .callout}


> ## Possible conflicts
>
> It might happen that `PATH` points to one environment first,
> while `LD_LIBRARY_PATH` points to libraries from another environment,
> which could cause either incorrect or hard-to-diagnose
> behavior later on. In general you should avoid manipulating those two
> variables manually.
{: .callout}


### PYTHONPATH - determine which Python module will be used

The idea of controlling resolution paths via environment variables
expands further into language specific domains. E.g., Python consults
the `PYTHONPATH` variable to possibly change the search paths for Python
modules.

> ## Possible side-effect
>
> Having a mix of system-wide and per-user installed
> apps/modules with custom
> installations in virtualenv environments can cause unexpected
> modules to be used.
>
> You can use `python -c 'import sys; print(sys.path)'` to output a
> list of paths your current default Python process would look through
> for Python libraries.
>
{: .callout}


### Additional aspects

> ## "Exported" vs. "local" variables
>
> Variables can be "exported" so they will be inherited by any new
> child process (e.g. when you start a new command in a shell). Otherwise
> the variable will be "local," and will not be inherited by child processes.
>
> 1. How could you determine if variable is exported or not?
> 2. Get a list of all local environments (present in your shell but
>  not exported)
>
> > ## Answers
> >
> > 1. Only exported variables will be output by `export` command. Or
> >    you could use `declare -p` to list all variable prepended with
> >    specification attribute:
> >    ~~~
> >    % LOCAL_VARIABLE="just for now"
> >    % export EXPORTED_VARIABLE="long live king"
> >    % declare -p | grep _VARIABLE
> >    declare -x EXPORTED_VARIABLE="long live king"
> >    declare -- LOCAL_VARIABLE="just for now"
> >    ~~~
> >    {: .bash}
> > 2. Extrapolate from 1.: `declare -p | grep -e '^declare --'`
> {: .solution}
{: .challenge}


## Efficient use of the interactive shell

A shell could be used quite efficiently if its features are learned and
it configured appropriately to simplify most common operations
performed in day to day activities.

### aliases

Aliases are simply shortcuts for most commonly used commands or add 
options to calls for most
common commands.  Please review some useful aliases presented in
[30 Handy Bash Shell Aliases For Linux / Unix / Mac OS X](https://www.cyberciti.biz/tips/bash-aliases-mac-centos-linux-unix.html).

> ## Should aliases defined in your `~/.bashrc` be used in your scripts?
>
> No. Since `~/.bashrc` is read only for interactive sessions,
> aliases placed there will not be available in your scripts'
> environment.  Even if they were available through some
> manipulations, it would be highly inadvisable to use them, since
> that would render your scripts not portable across machines/users.
{: .solution}

### Editing command line

`bash` and other shells use `readline` library for basic navigation
and manipulation of the command line entry.  That library provides two
major modes of operation which are inspired by
[two philosophically different editors](https://en.wikipedia.org/wiki/Editor_war)
-- `emacs` and `vim` .

Use **set -o emacs** to enter emacs mode (default), **set -o vi** to
enter vi mode. Further discussion and examples are for the default,
**emacs** mode. Learning navigation shortcuts could increase your
efficiency of working shell tenfold, so let's review most common ones
to edit the command line text

`Ctrl-a` | Go to the beginning of the line you are currently typing on
`Ctrl-e` | Go to the end of the line you are currently typing on
`Ctrl-l` | Clear the screen (similar to the clear command)
`Ctrl-u` | Remove text on the line before the cursor position
`Ctrl-h` | Remove preceding symbol (same as backspace)
`Ctrl-w` | Delete the word before the cursor
`Ctrl-k` | Remove text on the line after the cursor position
`Ctrl-t` | Swap the last two characters before the cursor
`Alt-t`  | Swap the last two words before the cursor
`Alt-f`  | Move cursor forward one word on the current line
`Alt-b`  | Move cursor backward one word on the current line
`Tab`    | Auto-complete files, folders, and command names

Hints:

- If `Alt-` combination does not work, you can temporarily workaround
  by hitting `Esc` key once instead of holding `Alt` before pressing
  following command character.
- Although many navigational commands could be achieved also by using
  "arrow keys" on your keyboard, some times using their `Ctrl-`
  counterparts is more efficient since it doesn't require you to move
  away your hands from the main alphanumeric portion of the keyboard.
- Many people find needing to use `Ctrl` key more often than
  `CapsLock` (originally used to assist FORTRAN and other languages
  programmers where all keywords had to be CAPITALIZED).  You could
  [change your environment settings](https://www.emacswiki.org/emacs/MovingTheCtrlKey)
  to either swap them or just make `CapsLock` into another `Ctrl` key.

If you need a more powerful way to edit current command line use

`Ctrl-x Ctrl-e` | (could be `Alt-e` in **zsh**) -- Edit command line text in the editor
                | (as defined by `VISUAL` environment variable)


In addition to ability to edit command line text, some shortcuts
control execution of the processes:

`Ctrl-c` | Kill currently running process
`Ctrl-d` | Exit current shell
`Ctrl-z` | Suspend currently running process. `fg` restores it, and `bg` would place it into background execution.

> ## set -o
>
> Shells provide a set of configurable options which could be enabled or
> disabled using `set` command.  Use `set -o` to print current settings
> you have in your shell, and then navigate `man bash` to find their
> extended description (in `man` search by using shortcut `/` and
> typing `o option-name`, and possibly 'n' for the "next" and 'p' for
> "previous" finding to identify corresponding section.
> E.g., use `set -o noclobber` which could be  recommended to forbid
> overwriting previously existing files. `>|` could be used to
> explicitly instruct overwriting already existing file. "Shell
> redirect ate my results file" should no longer be given as an excuse.
>
{: .challenge}

### Shell history

By default, a shell stores in memory a history of the commands you
have ran.  You could access it using `history` command.  When you exit
the shell, those history lines are appended to a file (by default in 
`~/.bash_history` for bash shell). This not
only allows to quickly recall commands you have ran recently, but
can provide you an actual "lab notebook" of the actions you have
performed. Thus the shell history could be indispensable to

- provide a skeleton for your script soon you realize that automating
  current operations is worthwhile the effort, and
- determine what exactly command you have ran to perform some given
  operation.

> ## Eternal history
>
> Unfortunately by default shell history is truncated to 1000 last
> commands, so you cannot use as your "eternal lab notebook" without
> some tuning.  Since it is a common problem, solutions
> exist, so please review available approaches:
> - [shell-chronicle](https://github.com/con/shell-chronicle)
> - [tune up of PROMPT_COMMAND](https://debian-administration.org/article/543/Bash_eternal_history)
>   to record each command as soon as it finished running
> - adjustment of `HISTSIZE` and `HISTCONTROL` settings,
>   e.g. [1](http://www.pointsoftware.ch/howto-bash-audit-command-logger/)
>   or [2](http://superuser.com/questions/479726/how-to-get-infinite-command-history-in-bash)
{: .callout}

Some of the main keyboard shortcuts to navigate shell history are:

`Ctrl-p` | Previous line in the history
`Ctrl-n` | Next line in the history
`Ctrl-r` | Bring up next match backwards in shell history

You can hit `Ctrl-r` and start typing some portion of the command you
remember running. Subsequent `Ctrl-r` will bring up the next match and so
on. You will leave "search" mode as soon as you use some other
command line navigation command (e.g. `Ctrl-e`).

`Alt-.` | Insert last positioned argument of the previous command.

Subsequent `Alt-.` will bring up the last argument of the previous command
and so on.

> ## History navigation exercise
>
> Inspect your shell command history you have run so far:
> 1. use `history` and `uniq` commands to find what is the most
>    popular command you have ran
> 2. experiment using `Ctrl-r` to find commands next to the most
>    popular command
{: .challenge}


## Hints for correct/robust scripting in shell

### Fail early

By default your shell script might proceed with execution even if some
command within it fails.  This might lead to very bad side-effects

- operating on incorrect results (e.g., if command re-generating
  results failed, but script continued)
- polluting the terminal screen (or log file) with output hiding away a
  point of failure

That is why it is generally advisable to use `set -e` in the scripts
that instructs the shell to exit with non-0 exit code right when some command fails.

> ## Note on special commands
> POSIX defines [some commands as "special"](https://www.gnu.org/software/bash/manual/html_node/Special-Builtins.html#Special-Builtins),
> failure in execution of which would cause entire script to exit (even
> without set `-e`) if they return non-0 value (`break`, `:`, `.`,
> `continue`, `eval`, `exec`, `exit`, `export`, `readonly`, `return`,
> `set`, `shift`, `trap`, `unset`).
{: .callout}

If you expect that some command might fail and it is OK, handle its
failing execution explicitly, e.g. via

~~~
% command_ok_to_fail || echo "As expected command_ok_to_fail failed"
~~~
{: .bash}

or just
~~~
% command_ok_to_fail || :
~~~
{: .bash}


### Use only defined variables

By default POSIX shell and bash treat undefined variables as variables
containing an empty string:

~~~
> echo ">$undefined<"
><
~~~
{: .bash}

which also could lead to many undesired and non-reproducible
or highly undesired side-effects:

- "using" mistyped variable names
- "using" variables which were not defined yet due to the logic
  in the script.  E.g. imagine effects of `sudo rm -rf ${PREFIX}/` if
  `PREFIX` variable was not defined for some reason.

The `set -u` option instructs the shell to fail if an undefined variable is
used.

If you intended to use some variable that might still be undefined
you could either use `${var:-DEFAULT}` to provide explicit `DEFAULT`
value or just define it conditionally on being not yet defined with:

~~~
% : ${notyetdefined:=1}
% echo ${notyetdefined}
1
~~~
{: .bash}


> ## set -eu
> Just set both "fail early" modes for extra protection to make your
> scripts more deterministic and thus reproducible.
{: .callout}


## (Unit)Testing

### Run-time testing

To some degree you could consider the `set -u` feature to be a "run time
test" -- "test if variable is defined, and if not -- fail".  **bash**
and other shells do actually provide a command called `test`, which
can perform various basic checks and return with non-0 exit code if
condition is not satisfied.  For undefined variable it is `test -v`:

~~~
% test -v undefined
% echo $?
1
~~~
{: .bash}

See "CONDITIONAL EXPRESSIONS" section of `man bash` page for more
conditions, such as

-a file   | True if file exists
-w file   | True if file exists and is writable
-z string | True if the length of string is non-zero

Alternatively to calling `test` command you could use
`[ TEST-EXPRESSION ]` syntax, so `test -v undefined` is identical to
`[ -v undefined ]`.

With `set -e` the whole operation of your script could be stated to be
somewhat tested -- script will fail as soon as any command fails.
Using such tests/assertions in your code could help guarantee that
your script performs as expected.

> Exercise: TODO

### Unit-testing

[Unit-testing](https://en.wikipedia.org/wiki/Unit_testing) is a
powerful paradigm to verify that pieces of your code (units) operate
correctly in various scenarios, and represent those assumptions in the
code.  An interesting observation is that everyone does "testing" by
simply running their code/scripts at least once on some inputs, 
seeing what they have produced, and checking if the output matches original
expectations. Unit-testing just takes it one step further -- code up
such tests in a separate file so you could run them all at once later
on (e.g. whenever you change your script) and verify that it still
performs correctly.  In the simplest case you could simply take your
test command and run them into a separate script that would fail if
any command within it fails, which would test your target script(s).  
For example, the following script could be used to test basic correct operation
of AFNI's `1dsum` command:

~~~
tfile=$(mktemp)              # create a temporary random file name
printf "1\n1.5\n" >| $tfile  # populate file with known data
result=`1dsum $tfile`        # compute result
[ "$result" = "2.5" ]        # compare result with target value
rm $tfile                    # cleanup
~~~
{: .bash}

Although looks uselessly simple, this is a powerful basic test
to guarantee that `1dsum` is available, that it is installed
correctly (matching architecture etc.), and operates fine on
typical files stored on the file system.

To have better management over collection of such tests, testing
frameworks were developed for shell scripts. Notable ones are:

- [shunit2: xUnit based unit testing for Unix shell scripts](https://code.google.com/archive/p/shunit2/)
- [Bats: Bash Automated Testing System](https://github.com/sstephenson/bats)

They provide helpers to exercise the tests and report which ones
passed and which failed, and to run a collection of tests.

> ## Exercise
>
> Choose shunit2 or bats (or both) and
>
> 1. re-write above test for `1dsum` using one of the frameworks.  If
> you do not have AFNI available, you could test generic `bc` or `dc`
> command line calculators possibly available on your system.
> 2. Add additional tests to "document" behavior of `1dsum` whenever
>   - input file is empty
>   - multiple files are provided
>   - some values are negative
{: .challenge}


> ## Testing frameworks
>
> Testing frameworks exist nearly for every programming and scripting
> language/environment. See [Wikipedia: List of unit testing frameworks](https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks)
{: .callout}
