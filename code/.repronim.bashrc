set -o noclobber  # do not overwrite existing files
set -o emacs  # use the emacs shortcuts

# function to help remind users about the shortcuts
print_shortcuts() {
LINE="Commandline/Cursor Editing Shortcuts::
Ctrl-a: Go to the beginning of the line you are currently typing on
Ctrl-e: Go to the end of the line you are currently typing on
Ctrl-u: Remove text on the line before the cursor position
Ctrl-h: Remove preceding symbol (same as backspace)
Ctrl-w: Delete the word before the cursor
Ctrl-k: Remove text on the line after the cursor position
Ctrl-t: Swap the last two characters before the cursor
Alt-t:  Swap the last two words before the cursor
Alt-f:  Move cursor forward one word on the current line
Alt-b:  Move cursor backward one word on the current line
Tab:    Auto-complete files, folders, and command names
Ctrl-x Ctrl-e OR Alt-e in zsh:  Edit command line text in the editor (as defined by VISUAL environment variable)"

CONTROL="Job Control Shortcuts::
Ctrl-c: Kill currently running process
Ctrl-d: Exit current shell
Ctrl-z: Suspend currently running process. fg restores it, and bg places it into background execution"

HISTORY="History Shortcuts::
Ctrl-p:	Previous line in the history
Ctrl-n:	Next line in the history
Ctrl-r:	Bring up next match backwards in shell history"

    if [ $# -lt 1 ]; then
        echo -e "${LINE}\n\n${CONTROL}\n\n${HISTORY}"
        return 0
    fi

    while [ $# -ge 1 ]; do
        case "$1"
        in
        n)
            echo -e "$LINE\n"
            shift;;
        line)
            echo -e "$LINE\n"
            shift;;
        c)
            echo -e "$CONTROL\n"
            shift;;
        control)
            echo -e "$CONTROL\n"
            shift;;
        h)
            echo -e "$HISTORY\n"
            shift;;
        history)
            echo -e "$HISTORY\n"
            shift;;
        -h)
            echo "Options are: n, line, c, control, h, history or blank"
            echo "Example1: print_shortcuts n c h"
            echo "Example2: print_shortcuts"
            return 0
            ;;
        --help)
            echo "Options are: n, line, c, control, h, history or blank"
            echo "Example1: print_shortcuts n c h"
            echo "Example2: print_shortcuts"
            return 0
            ;;
        *)
            echo "Option $1 not recognized use (n, line, c, control, h, history or blank)"
            echo "type print_shortcuts -h for help"
            echo "Example1: print_shortcuts n c h"
            echo "Example2: print_shortcuts"
            return 1
            ;;
        esac
    done
}


# create an eternal bash history file
# https://debian-administration.org/article/543/Bash_eternal_history

bhf="${HOME}/.bash_eternal_history"
if [ ! -f "${bhf}" ]; then
    touch "${bhf}"
fi

if [ "$(stat -c %a "${bhf}")" != "600" ]; then
    chmod 600 "${bhf}"
fi

# NOTE: I changed ${PROMPT_COMMAND:...} to ${PROMPT_COMMAND%%;:...}
# to account for trailing semicolons existing in the commmand (like if you've installed pyenv)
# see: https://github.com/pyenv/pyenv-virtualenv/issues/247
export HISTTIMEFORMAT="%s "
PROMPT_COMMAND="${PROMPT_COMMAND%%;:+$PROMPT_COMMAND ; }"'echo $$ $USER "$(history 1)" >> ${bhf}'

# make a terminal prompt that shows the full path: http://ezprompt.net/
export PS1="\[\e[33m\]\u\[\e[m\]:\[\e[35m\]\s\[\e[m\]\[\e[37m\]:\[\e[m\]\[\e[36m\]\w\[\e[m\]\\$ "
