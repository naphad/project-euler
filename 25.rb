def sol()
  n=3
  p1=1
  p2=1
  while true
    c=p1+p2
    p1=p2
    p2=c
    if (c.to_s.length >= 1000)
      break
    end
    n+=1
  end
  return n
end


puts sol()
