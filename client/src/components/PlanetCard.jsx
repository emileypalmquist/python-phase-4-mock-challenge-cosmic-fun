import React from 'react'

function PlanetCard({planet, image}) {
  return (
    <div className="planetCard">
        <img src={image} alt={planet.name} />
        <h4>Name: {planet.name}</h4>
    </div>
  )
}

export default PlanetCard
