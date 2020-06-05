# Propuesta Fiscal

## Introducción

Ésta es una propuesta de un esquema fiscal que en teoría busca:
* cobrar más impuestos a quienes tienen mayores utilidades (en base a flujo de efectivo, no en base a contabilidad),
* redistribuir esos impuestos de los que tienen mayores utilidades a los que tienen menores utilidades,
* cobrar más impuestos a aquéllos que tienen más riqueza que el resto,
* proporcionar un ingreso básico a toda la población,
* desincentivar el uso de efectivo,
* ser lo más sencillo posible para facilitar la determinación y pago de impuestos,
* evitar situaciones que pudieran ser aprovechadas por individuos para hacer estrategias que disminuyan el pago de impuestos.

Debe ser considerada como una idea para iniciar una discusión y buscar mejores soluciones; no como una propuesta completa, terminada e inamovible.


## Consideraciones generales

Se le asigna un Número de Identificación Único (*NIU* por ponerle un nombre) a cada persona del país (tanto física como moral):
* A las personas físicas se les asigna el NIU al nacer.
* A las personas morales se les asigna el NIU al momento de su constitución.

El Banco Central genera automáticamente una cuenta bancaria para cada persona asociada al NIU que no tendrá saldos mínimos, costos, ni comisiones para los usuarios.

Esta cuenta podrá ser usada únicamente para recibir y mandar dinero a otras cuentas. El Banco Central no ofrece ningún otro tipo de productos o servicios, ésos les corresponden a los bancos comerciales.

Cada transacción bancaria deberá de ser registrada con un identificador que, por ponerle un nombre, vamos a llamar *Tipo de transacción* (TT), así como un identificador único para esa transacción que le vamos a llamar *ID de Transaccción* (IDT) en base a la cual se le dará un tratamiento fiscal distinto.

El dinero en las cuentas bancarias no puede ser retirado en efectivo.

Se elimina el pago de liquidaciones e indemnizaciones por correr a los trabajadores. Si alguien se queda sin trabajo, cae automáticamente al menor nivel de ingresos y recibe sólo IBU.


## IVA

Todas las transacciones derivadas de la compra y venta de productos y servicios deberán tener el TT que las identifique como una compra-venta y pagarán una tasa de IVA.

Al realizar un pago el banco automáticamente le retendrá este IVA a quien recibe ese pago.

Todos los precios anunciados al público deberán incluir ya el IVA correspondiente.

Por ejemplo:
* Supongamos una tasa de IVA del 10%.
* Persona A le vende un producto por $100 pesos a Persona B.
* La Persona B hace un pago por $100 pesos a la Persona A.
* Persona A recibe $90 pesos, el banco retiene los $10 pesos y los paga al SAT.

Esto evita que la gente tenga que calcular y pagar impuestos, ya que el banco los recauda automáticamente con cada transacción.

Transacciones que no pagan IVA:
* transferencias entre cuentas de la misma persona,
* transferencias entre familiares en línea recta ascendente o descendente,
* transferencias entre hermanos,
* transferencias entre cónyuges,
* aportaciones de capital a personas morales,
* devoluciones de capital a accionistas,
* pago de dividendos,
* préstamos,
* capital repagado por préstamos otorgados (los intereses sí pagan IVA).


## Ingreso Básico Universal (IBU)
Se determinará un monto, el cual será depositado de manera mensual a la cuenta del Banco Central de cada persona física mes a mes.

El monto a recibir mensualmente deberá ser suficiente para pagar una vivienda modesta, alimentación y transporte; o sea para sobrevivir dignamente.

Este Ingreso Básico Universal también se suma a los ingresos para el cálculo de ISR.

Este pago será diferente e irá incrementándose dependiendo del grado escolar de cada persona:
* un monto para los niños antes de que entren a primaria,
* un monto para los niños de primaria,
* un monto para los niños de secundaria,
* un monto para los niños de preparatoria;
* todos los graduados de preparatoria reciben el mismo monto.


## Impuestos adicionales

### Inmuebles
El propietario de un inmueble pagará un impuesto predial que será determinado como un costo por m² de terreno dependiendo de la zona y el uso de suelo de cada lugar.

La autoridad deberá saber en todo momento si una propiedad está siendo ocupada por el propietario, por alguien más o desocupada:
* Si el propietario vive ahí paga normal
* Si está ocupada por otra persona paga normal, debe cobrar una renta
* Si está desocupada deberá pagar el impuesto correspondiente multiplicado por un factor (para desincentivar que la gente tenga propiedades que no ocupa).

Todos los propietarios de un inmueble estarán obligados a contratar una póliza de seguro que proteja el inmueble y de responsabilidad civil.

### Vehículos motorizados
El propietario de un vehículo motorizado pagará un impuesto de tenencia que será determinado como un porcentaje del valor original del vehículo.

Si una persona tiene más de un vehículo, multiplicará la tenencia por un factor multiplicador (si alguien puede tener más de un vehículo debe poder pagar más impuestos).

Todos los propietarios de un vehículo motorizado estarán obligados a contratar una póliza de seguro que proteja el vehículo y de responsabilidad civil.

### Herencias
Las herencias estarán exentas de pago de impuestos hasta un monto determinado, después de ese monto se pagará un porcentaje determinado.

El monto deberá ser determinado de tal manera que sólo la gente muy rica (digamos el 10% de la población del país) tenga que pagar este impuesto. Sin embargo el porcentaje a pagar sobre ese excedente debería ser muy elevado (90% o más).

El espíritu de esta disposición es que la gente más rica pueda dejarle un patrimonio considerable a sus hijos y regrese el resto al país.

### Impuesto a la riqueza
Aquellas personas que tengan dinero en el total de sus cuentas bancarias por arriba de un monto determinado deberán pagar un porcentaje sobre el excedente por encima de ese monto mensualmente.

Al igual que el impuesto a las herencias este monto deberá ser determinado de tal manera que sólo la gente muy rica caiga en este supuesto.

El monto a pagar por este impuesto no podrá exceder un porcentaje del valor total de las cuentas. Por ejemplo, no podría ser más que el 2% (dividido entre 12) del valor total en un mes determinado.

El valor total de las cuentas bancarias incluye la suma de los valores que estén invertidos en bonos, acciones y otros instrumentos de inversión, también lo que administren fideicomisos de los cuales esa persona tenga los derechos.

## Consideraciones finales
Hay muchos escenarios y casos que no funcionarían en la realidad actual. Habría que ir evaluando y buscando soluciones para cada uno. Algunos que se me ocurren:
* Este sistema requiere que todos tengan acceso a un dispositivo con Internet para realizar sus pagos. En una implementación real habría que buscar esquemas de transición para hacerle llegar los recursos, realizar transacciones y recaudar impuestos en lugares donde no se cuenta con Internet.
Probablemente esto se seguiría realizando mediante el uso de efectivo y los reportes manuales de cada persona, y el gobierno tendría que buscar la manera de poco a poco hacer llegar el Internet a todos los rincones del país (incluso a zonas donde no es rentable).
* No especifica cómo se pagan impuestos en transacciones con personas de otros países y en otras monedas.
* No provee un mecanismo para poner impuestos especiales para desincentivar el consumo de ciertos productos (tabaco, alcohol, alimentos y bebidas con alto contenido calórico, etc).
