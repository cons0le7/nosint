#!/bin/bash

chmod +x "$HOME/nosint/nosint"
chmod +x "$HOME/nosint/update.sh"
echo ""
echo "Update Successful. Press Enter to close script."
echo ""
read -p " >>> "
exec "$HOME/nosint/nosint"
exit 0
