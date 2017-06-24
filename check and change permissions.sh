#folders
find . -type d -perm 777 -exec chmod 755 {} \;

#files
find . -type f -perm 777 -exec chmod 644 {} \;
