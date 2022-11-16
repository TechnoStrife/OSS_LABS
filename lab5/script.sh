#!/bin/bash
ps -eo euser,ruser,comm | tail -n +2 | awk '{if ($1 != $2) print $3}'
