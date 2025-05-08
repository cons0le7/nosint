#!/bin/bash

chmod +x "$HOME/nosint/nosint"
chmod +x "$HOME/nosint/update.sh"
echo ""
echo "Update Successful. Press Enter to reload script."
echo ""
echo "reloading... "
sleep 1 
"$HOME/nosint/nosint"

