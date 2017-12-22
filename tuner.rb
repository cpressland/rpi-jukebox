#!/usr/bin/env ruby

require 'sinatra'

set :port, 80
set :bind, '0.0.0.0'

get "/station/:name" do |a|
  case a
  when 'classicrock'
    n = 'Absolute Classic Rock'
    u = 'http://mp3-ac-128.timlradio.co.uk/'
  when 'absoluteradio'
    n = 'Absolute Radio'
    u = 'http://mp3-ar-128.timlradio.co.uk/'
  when 'kerrang'
    n = 'Kerrang Radio'
    u = 'http://live-bauer-al.sharp-stream.com/kerrang.mp3'
  when 'heartextra'
    n = 'Heart Extra'
    u = 'http://media-the.musicradio.com/Heartextra'
  when 'radiox'
    n = 'Radio X'
    u = 'http://media-sov.musicradio.com/RadioXLondon'
  else
    halt 404
  end

  File.write('/tmp/jukebox.env', "STATION=#{u}\n")
  system 'systemctl restart jukebox.service'
  status 200
  body "Playing #{n}"
end

get "/control/:status" do |a|
  unless ['start', 'stop', 'restart'].include?(a)
    halt 404
  end

  system "systemctl #{a} jukebox.service"
  status 200
  body "#{a.capitalize}ing Jukebox"
end
