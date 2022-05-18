#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <experimental/random>
#include <queue>
#include <vector>

enum color {
	WHITE = 0,
	GREY,
	BLACK,
};

size_t *M;
color *visited;
size_t rows = 0;	//Cuantas filas hay
size_t cols = 0;	//Cuantas columnas hay

std::vector<size_t>
adjacents(size_t v) {
	std::vector<size_t> adj;
	size_t c = v % cols; //en que columna esta
	size_t f = (v - c) / cols;
	if (c > 0) {
		if (M[v - 1] == 1) adj.push_back(v - 1);
	}
	if (c < cols - 1) {
		if (M[v + 1] == 1) adj.push_back(v + 1);
	}
	if (f > 0) {
		if (M[(f - 1) * cols + c] == 1) adj.push_back((f - 1) * cols + c);
	}
	if (f < rows - 1) {
		if (M[(f + 1) * cols + c] == 1) adj.push_back((f + 1) * cols + c);
	}
	return adj;
}

void
bfs(size_t v) {
	std::queue<size_t> queue;
	queue.push(v);

	while (queue.size() > 0) {
		size_t w = queue.front();
		queue.pop();
		for (auto u : adjacents(w)) {
			if (visited[u] == WHITE) {
				visited[u] = GREY;
				queue.push(u);
			}
		}
		visited[w] = BLACK;
	}
}

size_t
count_components() {
	size_t comps = 0;
	for (size_t v = 0; v < cols * rows; v++) {
		if (M[v] == 1 && visited[v] == WHITE) {
			bfs(v);
			comps++;
		}
	}
	return comps;
}

int
main() {
//	std::cin >> rows >> cols;
//	M = (size_t *)calloc(cols * rows, sizeof(size_t));
//	visited = (color *)calloc(cols * rows, sizeof(color));

//	unsigned char c = 0;
//	for (size_t i = 0; i < cols * rows; i++) {
//		std::cin >> c;
//		M[i] = c - '0';
//	}

	rows = std::experimental::randint(1,5000);
	cols = std::experimental::randint(1,5000);

	M = (size_t *)calloc(cols * rows, sizeof(size_t));
	visited = (color *)calloc(cols * rows, sizeof(color));

	std::cout << rows << ' ' << cols << std::endl;

	for (size_t i = 0; i < cols * rows; i++) {
		M[i] = std::experimental::randint(0, 1);
		if (i != 0 && i % cols == 0) std::cout << std::endl;
		std::cout << M[i];
	}

	std::cout << std::endl << count_components() << std::endl;
	free(M);
	free(visited);
}
