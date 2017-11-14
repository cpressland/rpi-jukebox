#!/usr/bin/env ruby

def station
  a = ARGV[1]

  case a
  when 'classicrock'
    n = 'Absolute Classic Rock'
    u = 'http://mp3-ac-128.timlradio.co.uk/'
  when 'absoluteradio'
    n = 'Absolute Radio'
    u = 'http://mp3-ar-128.timlradio.co.uk/'
  else
    abort("Not a valid option, try 'classicrock' or 'absoluteradio'")
  end

  File.write('/etc/jukebox.env', "STATION=#{u}\n")
  puts "Playing #{n}"
  system 'systemctl restart jukebox.service'
end

def control
  a = ARGV[1]

  unless ['start', 'stop', 'restart'].include?(a)
    abort("#{a} is not valid, use start, stop or restart")
  end

  puts "#{a.capitalize}ing Jukebox"
  system "systemctl #{a} jukebox.service"
end

if ARGV[0] == 'station'
  station
elsif ARGV[0] == 'control'
  control
end
