BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "charts_ativo" (
	"id"	integer NOT NULL,
	"nome_ativo"	varchar(10) NOT NULL,
	"valor_strike"	real NOT NULL,
	"vencimento"	date NOT NULL,
	"am_europeia"	varchar(2) NOT NULL,
	"call_put_papel"	varchar(2) NOT NULL,
	"formador_mercado"	varchar(2) NOT NULL,
	"empresa"	varchar(18) NOT NULL,
	"data_criacao_tabela"	datetime NOT NULL,
	"habilitado"	bool NOT NULL,
	"on_pn"	varchar(2) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "charts_ativo" ("id","nome_ativo","valor_strike","vencimento","am_europeia","call_put_papel","formador_mercado","empresa","data_criacao_tabela","habilitado","on_pn") VALUES (1,'PETRE409',38.09,'2022-05-20','AM','CA','','Petrobras','2022-04-23 16:18:26',1,'PN'),
 (2,'PETRQ254',25.09,'2022-05-20','EU','PU','','Petrobras','2022-04-23 16:18:26',1,'PN');
COMMIT;
