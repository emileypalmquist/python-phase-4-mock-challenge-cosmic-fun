import React from 'react'
import { Link } from 'react-router-dom'
import { SuspenseImg } from './SuspenseImage'

function ScientistCard({scientist: {id, name, avatar}, onDelete}) {
  return (
    <div className="scicard">
        <SuspenseImg src={avatar} alt={name} />
        <h3>{name}</h3>
        <Link to={`/scientists/${id}`}>View Missions</Link>
        <span> <button onClick={()=>onDelete(id)}><strong>X</strong></button></span>
    </div>
  )
}

export default ScientistCard