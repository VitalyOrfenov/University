
CREATE TABLE Craftsman
(
	cftmn_id             SMALLINT NOT NULL Primary Key ,
	fn_sn_cftmn          VARCHAR(70) NOT NULL ,
	contact_numb_cftmn   VARCHAR(16) NOT NULL ,
	e_mail_cftmn         VARCHAR(50) NULL ,
	address_cftmn        VARCHAR(100) NOT NULL ,
	speciality_cftmn     VARCHAR(40) NOT NULL ,
	expnc_cftmn          SMALLINT NOT NULL 
);
SELECT * FROM projectlist_forcEO
(
	mng_id               SMALLINT NOT NULL Primary Key,
	fn_sn_mng            VARCHAR(70) NOT NULL ,
	contact_numb_mng     VARCHAR(16) NOT NULL ,
	e_mail_mng           VARCHAR(50) NULL ,
	address_mng          VARCHAR(100) NOT NULL 
);
SELECT * FROM PROJECT
DELETE FROM project_jrnl
CREATE TABLE Material
(
	mat_type             VARCHAR(25) NOT NULL ,
	discrip              VARCHAR(55) NOT NULL ,
	order_id             SMALLINT NOT NULL
);

ALTER TABLE Material
	ADD CONSTRAINT  XPKMaterial PRIMARY KEY (mat_type,order_id);

CREATE TABLE Orderer
(
	orderer_id           SMALLINT NOT NULL PRIMARY KEY,
	fn_sn_orderer        VARCHAR(70) NOT NULL ,
	contact_numb_orderer VARCHAR(16) NOT NULL ,
	e_mail_orderer       VARCHAR(50) NULL ,
	address_orderer      VARCHAR(150) NOT NULL ,
	mng_id               SMALLINT NOT NULL 
);


CREATE TABLE Project
(
	order_id             SMALLINT NOT NULL PRIMARY KEY,
	begin_date           DATE NOT NULL,
	end_date             DATE NOT NULL,
	price                MONEY NOT NULL,
	progress             SMALLINT NOT NULL,
	stage                VARCHAR(20) NOT NULL,
	orderer_id           SMALLINT NOT NULL,
	cftmn_id             SMALLINT NOT NULL 
);

ALTER TABLE PROJECT
    ADD CONSTRAINT PKProject PRIMARY KEY (order_id)

ALTER TABLE Material
	ADD CONSTRAINT consist_of_needed_in FOREIGN KEY (order_id) REFERENCES Project (order_id);

ALTER TABLE Orderer
	ADD CONSTRAINT help_guided_by FOREIGN KEY (mng_id) REFERENCES Manager (mng_id);

ALTER TABLE Project
	ADD CONSTRAINT formulate_belong_to FOREIGN KEY (orderer_id) REFERENCES Orderer (orderer_id);

ALTER TABLE Project
	ADD CONSTRAINT produce_produced_by FOREIGN KEY (cftmn_id) REFERENCES Craftsman (cftmn_id);


INSERT INTO Manager
VALUES  (256, '������� �.�.', '87548238574', 'morozzz@gmail.com', '��. ��������, ��� 15, ��.45'),
		(312, '�������� �.�.', '89156654875', 'crowtsov@yandex.ru', '��. ���������, ��� 112, ��. 12'),
		(123, '��������� �.�.', '89035656468', 'vasvasvas@gmail.com', '��. �������, �.15, ��.119'),
		(523, '�������� �.�.', '89647513355', 'ColdoffDM@ramler.ru', '������� ��., �.67, ��.15'),
		(142, '�������� �.�', '89425642354', 'kamenevaks@yandex.ru', '��������� ��., �.12�, ��.144'),
		(698, '������ �.�', '89092554235', 'Shneigdar@gmail.com', '��. �������, �.20, ��. 17'),
		(900, '�������� �.�', '89754453215', 'sholopaichik@mail.ru', '��. �������, �.20, ��.100');


INSERT INTO Craftsman
VALUES  (711 , '��������� �.�.', '897777777', NULL , '��. ���������, �. 12, ��. 42', '������ �� ���', 25),
		(864 , '���������� �.�.', '89542365412', 'schwarznegger@gmail.com', '��. ��������, �.24, ��.6', '������ �� ���', 17),
		(486 , '������������ �.�.', '89465216545', 'illbeback@term.com', '��. �������, �.23, ��. 72', '������ �� ���', 23),
		(212 , '������� �.�', '87622168546', 'rockybalboa@stallone.en', '��. ��������, �.17, ��. 22', '������ �� ����', '24'),
		(055 , '���������� �.�', '89647842354', NULL , '��. ��������, �.153, ��.14', '����������� (���)', '7'),
		(999 , '��������� �.�', '89325454685', 'louisarmstrong@jazzmail.com', '��. ���������, �.29, ��.75', '����������� (����)', '10'),
		(172 , '�������� �.�', '89455135424', 'kirch725@yandex.ru', '��. �������������, �.25, ��. 130', '����������� (���)', '5');


INSERT INTO Orderer
VALUES	(717 ,'������ �.�.', '89032293221', 'qwertybit@mail.ru', '��. �����������, �.16�3, ��.155', 523),
		(125 , '���������� �.�.', '89060605532', 'tujh12@rambler.ru', '��. ���������, �.10, ��. 81', 900),
		(872 , '������� �.�.', '89070705468', 'tujh13@gmail.com', '��. �����������, �.14, ��.85', 698),
		(275 , '�������� �.�.', '89675243687', 'momimba97@mail.ru', '��. �������, �.17, ��. 110', 123),
		(936 , '����������� �.�', '89015462135', 'barancevicvpered@yandex.ru', '��. �����������, �.54, ��. 167', 142);

INSERT INTO Project
VALUES (100, '2018-05-18', '2018-12-16', 180000, 80, '��������� ���������', 717, 711),
	   (298, '2018-10-12', '2019-07-21', 256000, 30, '�������� ������', 125, 711),
	   (765, '2018-12-09', '2019-06-09', 145000, 0, '���������� �����������', 872, 212),
	   (351, '2018-11-11', '2019-05-17', 200000, 20, '���������� ������� � �����', 275, 711),
	   (942, '2018-09-09', '2019-09-18', 350000, 10, '����������� �����', 936, 486);

INSERT INTO MATERIAL
VALUES ('��������� ����', '��������, ����� LP', 100, 717), ('��������� ��������', '���������', 100, 717 ),
	   ('��������� �����', '��������', 100, 717 ), ('��������������1', 'Seymour Duncan SH-55', 100, 717 ),
	   ('��������������2', 'SEYMOUR DUNCAN SH-55', 100, 717 ), ('�����', 'Tune-o-Matic', 100, 717 ),

	   ('��������� ����', '��������, ����� Dean ML', 298, 125), ('��������� ��������', '������ ������', 298, 125),
	   ('��������� �����', '��������', 298, 125), ('��������������1', 'Seymour Duncan SH-13 Dimebucker', 298, 125),
	   ('��������������2', 'Seymour Duncan SH-1 59 Humbucker', 298, 125), ('�����', 'Floyd Rose (�-�)', 298, 125),

	   ('��������� ����', '�����, ����� Telecaster', 765, 872), ('��������� ��������', '����', 765, 872),
	   ('��������� �����', '����', 765, 872), ('��������������1', 'Fender CS "51 Nocaster"', 765, 872),
	   ('��������������2', '-', 765, 872),('�����', 'GOTOH Nickel Bridge (Hardtail)', 765, 872), 

	   ('��������� ����', '����, ����� Superstrat', 351, 275), ('��������� ��������', '���������', 351, 275), 
	   ('��������� �����', '����', 351, 275), ('��������������1', 'EMG 81', 351, 275), 
	   ('��������������2', 'EMG 60', 351, 275),	('�����', 'Ibanez Edge PRO (�-�)', 351, 275), 

	   ('��������� ����', '����, ����� Mustang', 942, 936), ('��������� ��������', '������ ������', 942, 936), 
	   ('��������� �����', '����', 942, 936), ('��������������1', 'Fernandes FSK-401 Sustainer Bridge (Sustainiac)', 942, 936), 
	   ('��������������2', 'Manson MBK-2', 942, 936), ('�����', 'Tune-O-Matic x Stop Bar', 942, 936), 
	   ('��������� MIDI-������', 'Manson MIDI Controller Screen', 942, 936), ('��������� �����', '12 ����� ����������� + ����� ��������', 942, 936);

CREATE INDEX orderername
ON Orderer (fn_sn_orderer)

CREATE INDEX mat_type
ON Material (mat_type)

CREATE INDEX mng_of_orderer
ON Orderer (mng_id)

CREATE VIEW craftsmanlist AS SELECT fn_sn_cftmn, e_mail_cftmn, speciality_cftmn, expnc_cftmn FROM Craftsman

CREATE VIEW projectlist_forCEO AS SELECT order_id, progress, stage, price, begin_date, end_date FROM Project

CREATE VIEW securitylist AS SELECT fn_sn_cftmn, contact_numb_cftmn FROM Craftsman UNION SELECT fn_sn_mng, contact_numb_mng FROM Manager

CREATE TABLE project_jrnl (order_id             SMALLINT NOT NULL,
						   begin_date           DATE NOT NULL,
						   end_date             DATE NOT NULL,
						   price                MONEY NOT NULL,
						   progress             SMALLINT NOT NULL,
						   stage                VARCHAR(20) NOT NULL,
						   orderer_id           SMALLINT NOT NULL,
						   cftmn_id             SMALLINT NOT NULL,
						   change_date		   DATE NOT NULL)

CREATE TRIGGER project_journal
ON Project
AFTER UPDATE
AS 
IF @@ROWCOUNT > 1
BEGIN
ROLLBACK TRAN
RAISERROR ('�� ���� ��� ����� ������� ������ ���� ������.', 16, 10)
END
IF UPDATE (progress)
IF EXISTS(SELECT * 
		  FROM Project P 
		  WHERE P.progress = 100)
BEGIN
DECLARE @id SMALLINT
DECLARE	@begin_date DATE
DECLARE	@end_date DATE 
DECLARE	@price MONEY
DECLARE	@progress SMALLINT
DECLARE	@stage VARCHAR(20) 
DECLARE	@orderer_id SMALLINT
DECLARE	@cftmn_id SMALLINT

SELECT @id = (SELECT order_id FROM Project P WHERE P.progress = 100)
SELECT @begin_date = (SELECT begin_date FROM Project P WHERE P.progress = 100)
SELECT @end_date = (SELECT end_date FROM Project P WHERE P.progress = 100)
SELECT @price = (SELECT price FROM Project P WHERE P.progress = 100)
SELECT @progress = (SELECT progress FROM Project P WHERE P.progress = 100)
SELECT @orderer_id = (SELECT orderer_id FROM Project P WHERE P.progress = 100)
SELECT @cftmn_id = (SELECT cftmn_id FROM Project P WHERE P.progress = 100)
INSERT INTO project_jrnl
VALUES (@id, @begin_date, @end_date, @price, @progress, '������ ����', @orderer_id, @cftmn_id, GETDATE())

DELETE FROM Material
WHERE order_id = (SELECT order_id 
				  FROM Project P	
				  WHERE P.progress = 100)
DELETE FROM Project 
WHERE Project.progress = 100
END;

CREATE PROCEDURE expnc_lvlup @cftmnid SMALLINT
AS 
BEGIN
UPDATE Craftsman SET expnc_cftmn = 
expnc_cftmn + 1 WHERE cftmn_id = @cftmnid
END;

EXECUTE expnc_lvlup 864
SELECT * FROM craftsman

UPDATE Craftsman SET expnc_cftmn = 17 WHERE cftmn_id = 864


UPDATE Project SET Progress = 100 WHERE order_id = 100

