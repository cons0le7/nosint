#!/bin/bash

chmod +x "$HOME/nosint/nosint"
chmod +x "$HOME/nosint/update.sh"
echo ""
echo "Update Successful."
echo ""
echo "reloading tool... "
sleep 1 
sh -c "$HOME/nosint/nosint"
exit 0

