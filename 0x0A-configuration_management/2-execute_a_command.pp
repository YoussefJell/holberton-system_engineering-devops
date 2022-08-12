# kills the killmenow process
exec { 'kill-proc'
  command => 'pkill -f killmenow'
}
