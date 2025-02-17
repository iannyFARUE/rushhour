import unittest
from core.dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        # graph = {
        #     'A':[('B', 1), ('C', 2)],
        #     'B':[('D',2)],
        #     'C':[('D',2)],
        # }
        
        graph = {
            'A': {'B': 1, 'C': 2},
            'B': {'D': 2},
            'C': {'D': 2},
            'D': {}
        }
        
        expected_distance = 3
        expected_path = ['A', 'B', 'D']
        source = 'A'
        destination = 'D'
        result = dijkstra(graph, source, destination)
        self.assertEqual(result['distance'], expected_distance)
        self.assertEqual(result['path'], expected_path)
        
if __name__ == '__main__':
    unittest.main()
        
        