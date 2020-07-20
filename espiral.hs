--Dada una matriz, retornar una lista de sus valores leidos en forma de espiral 
--en sentido horario empezando desde la posición (x,y)=(0,0)

transpose:: [[a]]->[[a]]
transpose ([]:_) = []
transpose x = [(map head x)] ++ transpose (map tail x)

spiralList :: [[a]] -> [a] 
spiralList [(x:xs)] = (x:xs)
spiralList (x:xs) = x ++ (spiralList (reverse (transpose xs)))