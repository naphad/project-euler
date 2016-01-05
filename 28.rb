s = 1
l = 1
(3..1001).select(&:odd?).each do |x|
  inc = 2*((x/2)-1)+2
  s += (l+inc..l+inc*4).step(inc).reduce(&:+) # next 4 numebrs with inc between
  # them
  l = l+inc*4
end
puts s
