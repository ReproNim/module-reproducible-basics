
set -o noclobber
set -o emacs

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
Ctrl-x OR Ctrl-e OR Alt-e in zsh:  Edit command line text in the editor (as defined by VISUAL environment variable)"
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
            echo "Options are: n, line, c, control, h, history or nothing at all"
            return 0
            ;;
        *)
            echo "Option $1 not recognized use (n, line, c, control, h, history or nothing at all)"
            return 1
            ;;
        esac
    done
}


# https://debian-administration.org/article/543/Bash_eternal_history

bhf="${HOME}/.bash_eternal_history"
if [ ! -f "${bhf}" ]; then
    touch "${bhf}"
fi

if [ "$(stat -c %a "${bhf}")" != "600" ]; then
    chmod 600 "${bhf}"
fi

export HISTTIMEFORMAT="%s "
PROMPT_COMMAND="${PROMPT_COMMAND%%;:+$PROMPT_COMMAND ; }"'echo $$ $USER "$(history 1)" >> ${bhf}'

# make a prompt: http://ezprompt.net/
export PS1="\[\e[33m\]\u\[\e[m\]:\[\e[35m\]\s\[\e[m\]\[\e[37m\]:\[\e[m\]\[\e[36m\]\w\[\e[m\]\\$ "