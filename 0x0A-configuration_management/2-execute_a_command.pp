# kills the killmenow process
exec { 'kill-proc'
  command => '/usr/bin/pkill -f killmenow'
}
