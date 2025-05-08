#!/bin/bash

chmod +x "$HOME/nosint/nosint"
chmod +x "$HOME/nosint/update.sh"
echo ""
echo "Update Successful. Press Enter to close script."
echo ""
read -p " >>> "
nosint
exit 0
