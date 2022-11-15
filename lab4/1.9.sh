#!/bin/bash
ps -Fe --sort rss | tail -n +2 -n 5 | tac
