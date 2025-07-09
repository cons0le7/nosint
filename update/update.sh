#!/usr/bin/bash

HOME_PATH="$HOME/nosint"
REPO_URL="https://github.com/cons0le7/nosint.git"

if [ ! -d "$HOME_PATH" ]; then
    echo ""
    git clone "$REPO_URL" "$HOME_PATH" 
    chmod +x "$HOME_PATH/update/update.sh"
    chmod +x "$HOME_PATH/update/update_2.sh"
    exec "$HOME_PATH/update/update_2.sh"
    exit 0
else
    echo ""
    git -C "$HOME_PATH" fetch
    BRANCH_NAME=$(git -C "$HOME_PATH" rev-parse --abbrev-ref HEAD)
    git -C "$HOME_PATH" reset --hard "origin/$BRANCH_NAME"
    chmod +x "$HOME_PATH/update/update.sh"
    chmod +x "$HOME_PATH/update/update_2.sh"
    exec "$HOME_PATH/update/update_2.sh"
    exit 0 
fi
