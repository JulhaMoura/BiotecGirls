import sqlite3

classe  Db ( objeto ):
	'' 'A classe Db representa ou banco de dados, ela guarda os seguintes objetos
	conn = conexão
	cursor = cursor para executar instruções sql
	'' '
	def  __init__ ( self ):
		eu . conn  =  sqlite3 . connect ( 'Clientes.db' )
		eu . cursor  =  próprio . conn . cursor ()
        