#!/bin/bash
echo "Домашний каталог пользователя"
echo "$USER"
echo "содержит обычных файлов:"
find ~ -maxdepth 1 -type f -not -name ".*" | wc -l
echo "содержит скрытых файлов:"
find ~ -maxdepth 1 -type f -name ".*" | wc -l
