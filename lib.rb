# time of block in ms
def time
  t0 = Time.now
  yield
  t1 = Time.now
  (t1-t0) * 1000
end
