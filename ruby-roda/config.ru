require 'roda'
require 'json'

class App < Roda

  route do |r|

    r.root do
      'Hello World!'
    end

    r.on 'api' do

      r.response['Content-Type'] = 'application/json'

      r.on 'current-time' do
        {'timestamp'=>Time.now.to_i.to_s}.to_json
      end

      r.on 'bigdata' do
        h = {}
        2000.times do |k|
          h[k] = x = []
          99.downto(0) { |i| x << i }
        end
        h.to_json
      end

      r.on Integer, /([a-z]+)/ do |i, rxp|
        {'int'=>i, 'regex'=>rxp}.to_json
      end

    end

  end

end

run App.freeze
