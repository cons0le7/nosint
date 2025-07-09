#!/usr/bin/bash

echo ""
echo "Are you sure you want to uninstall? (y/n): "
echo ""
read -r confirm
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    exit
fi
echo ""
echo "Removing '~/nosint'..."
rm -rf "$HOME/nosint"
echo "success"
echo ""
symlink_paths=(
    "/usr/bin/nosint"
    "/data/data/com.termux/files/usr/bin/nosint"
    "/usr/local/bin/nosint"
)
for link_path in "${symlink_paths[@]}"; do
    if [ -L "$link_path" ] || [ -e "$link_path" ]; then
        echo "Removing '$link_path'... "
        rm "$link_path"
        echo "success"
    else
        continue
    fi
done
echo ""
echo "Deleting stored api.key..."
rm -f "$HOME/.nosint/api.key"
echo "success"
echo ""
echo "Do you want to delete all saved data in '~/.nosint'? (y/n): "
echo ""
read -r choice
if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
    rm -rf "$HOME/.nosint"
    echo ""
    echo "Saved data deleted."
else
    echo ""
    echo "Saved data retained."
fi
echo "" 
echo "nosint uninstalled successfully." 
echo ""
