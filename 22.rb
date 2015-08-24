# simple data processing

def name_val(name)
  subscore ||= 0
  name.each_char{|c| subscore += (c.ord-'A'.ord+1)}
  return subscore
end

names = []
File.foreach("./data/22/names.txt") {|x| names.push(*(x.delete('"').split(','))) } # better to break it up then to slurp b/c of increasing alloc/dealloc overhead
names = names.sort

score ||= 0
names.each_with_index{|name, index| score += name_val(name)*(index+1)}

puts "Answer is: #{score}"
