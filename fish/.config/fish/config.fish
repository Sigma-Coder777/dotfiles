if status is-interactive
    # Commands to run in interactive sessions can go here
end
set fish_greeting
colorscript random
# Starship prompt
starship init fish | source

thefuck --alias | source
