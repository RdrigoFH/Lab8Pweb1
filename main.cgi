#!/usr/bin/perl
use strict;
use warnings;
use CGI;

my $cgi = new CGI;

my $numero1 = $cgi->param('numero1');
my $numero2 = $cgi->param('numero2');

my $resultado;
if ($operacion eq '+') {
    $resultado = $numero1 + $numero2;
} elsif ($operacion eq '-') {
    $resultado = $numero1 - $numero2;
} elsif ($operacion eq '*') {
    $resultado = $numero1 * $numero2;
} elsif ($operacion eq '/') {
    if ($numero2 != 0) {
        $resultado = $numero1 / $numero2;
    } else {
        $resultado = "Error: No puedes divider entre 0";
    }
} else {
    $resultado = "Error: Operacion no válida";
}
print $cgi->header('text/html');
print <<END_HTML;
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Resultado</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <h2>Resultado:</h2>
  <p>$numero1 + $numero2 = $resultado</p>

</body>
</html>
END_HTML
