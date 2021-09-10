export class Ship {
  constructor(name, size) {
    this.name = name;
    this.size = size;
    this.squares = [];
    this.hitSquares = [];
    this.placed = false;
    this.destroyed = false;
  }

  ocupiesSquare(i, j) {
    return (
      this.squares.filter((square) => square[0] === i && square[1] === j)
        .length > 0
    );
  }

  isSquareHit(i, j) {
    return (
      this.hitSquares.filter((square) => square[0] === i && square[1] === j)
        .length > 0
    );
  }

  processHit(i, j) {
    if (this.ocupiesSquare(i, j) && !this.isSquareHit(i, j)) {
      this.hitSquares.push([i, j]);
    }

    if (this.hitSquares.length === this.size) {
      this.destroyed = true;
    }
  }
}

export function parseConfiguration(config) {
  let ships = config.map((ship) => {
    let shipObj = new Ship(ship.name, ship.size);
    shipObj.squares = ship.squares;
    shipObj.placed = true;
    return shipObj;
  });
  return ships;
}
