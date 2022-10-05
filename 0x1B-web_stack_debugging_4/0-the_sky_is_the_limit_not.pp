# Fix nginx user limit
exec { 'fix-nginx':
  command => '/bin/sed -i s/15/4096/ /etc/default/nginx && sudo service nginx restart'
}
