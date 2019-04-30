SELECT * 
FROM Material
WHERE order_id = (SELECT order_id 
				  FROM Project
				  WHERE (SELECT MAX(price) 
					     FROM Project) = price)

SELECT O.fn_sn_orderer, O.contact_numb_orderer, P.begin_date, P.end_date, P.price, P.progress, P.stage
FROM Orderer O INNER JOIN Project P
ON O.orderer_id = P.orderer_id

SELECT M.fn_sn_mng, M.contact_numb_mng, M.e_mail_mng, O.fn_sn_orderer, O.contact_numb_orderer, O.address_orderer
FROM Orderer O RIGHT JOIN Manager M
ON O.mng_id = M.mng_id

SELECT C.fn_sn_cftmn, C.speciality_cftmn, C.expnc_cftmn, P.begin_date, P.end_date, P.stage, P.progress
FROM Craftsman C LEFT JOIN Project P 
ON C.cftmn_id = P.cftmn_id

SELECT C.fn_sn_cftmn, C.speciality_cftmn, C.expnc_cftmn
FROM Craftsman C
WHERE C.speciality_cftmn LIKE 'Подмастерье%'

SELECT COUNT(P.cftmn_id) as 'Кол-во проектов', C.fn_sn_cftmn, C.speciality_cftmn
FROM Project P LEFT JOIN Craftsman C
ON P.cftmn_id = C.cftmn_id
GROUP BY P.cftmn_id, C.fn_sn_cftmn, C.speciality_cftmn

SELECT *
FROM Material M
WHERE M.order_id = (SELECT M.order_id 
					FROM Material M 
					WHERE M.discrip LIKE 'Махагони% ML%')

