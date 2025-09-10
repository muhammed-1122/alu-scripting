#!/usr/bin/env ruby
line = ARGV[0] || ""
# capture from, to and flags fields inside square brackets
m = line.match(/\[from:([^\]]+)\].*?\[to:([^\]]+)\].*?\[flags:([^\]]+)\]/)
puts "#{m[1]},#{m[2]},#{m[3]}" if m
