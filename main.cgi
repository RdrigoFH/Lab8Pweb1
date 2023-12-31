#!/usr/bin/perl
use strict;
use warnings;
use CGI;

# Crea una nueva instancia CGI
my $cgi = new CGI;

# Obtiene los valores ingresados en el formulario
my $numero1 = $cgi->param('numero1');
my $numero2 = $cgi->param('numero2');

# Realiza la operación de suma
my $resultado = $numero1 + $numero2;

# Imprime el encabezado HTTP y la respuesta
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
