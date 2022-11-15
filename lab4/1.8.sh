#!/bin/bash
echo "Процессов пользователя:"
echo "$USER"
ps aux | cut -d' ' -f1 | grep $USER | wc -l
echo "Процессов пользователя root:"
ps aux | cut -d' ' -f1 | grep root | wc -l
