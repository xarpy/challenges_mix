SELECT SUPPLIER.SUPPLIER_NAME AS SUPPLIERS, PART.PRICE AS PRICE
FROM SUPPLIER
LEFT JOIN SUPPLY ON SUPPLIER.SUPPLIER_CODE = SUPPLY.CODE_SUPPLIER
LEFT JOIN PART ON SUPPLY.CODE_PIECE = PART.CODE_PART
JOIN CAR ON SUPPLY.CODE_CAR = CAR.CODE_CAR
WHERE SUPPLIER.CITY = "VITORIA" AND PART.CODE_PART = "MOTOR" AND CAR.CODE_CAR = "KOMBI";