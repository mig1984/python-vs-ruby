require 'json'

now = Time.now

1000.times do
  h = {}
  2000.times do |k|
    h[k] = x = []
    99.downto(0) { |i| x << i }
  end
end

puts now-Time.now

