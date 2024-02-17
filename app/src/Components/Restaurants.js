import React from 'react'

export default function Restaurants({restaurants, setRestaurants}) {
	function handleDelete(id){
		fetch(`http://127.0.0.1:5500/restaurants/${id}`, {
			method:'DELETE'
		}).then(res => res.json())
		.then(() => {
			let filtered_restaurants = restaurants.filter(restaurant => {
				return restaurant.rest_id !== id;
			})
			setRestaurants(filtered_restaurants)
		})
	}

	let rest_list = restaurants.map(restaurant => {
		return(
			<div key={restaurant.rest_id} className='card m-2 p-2'>
				<h3>{restaurant.rest_id}</h3>
				<p>Name: {restaurant.name}</p>
				<p>Address: {restaurant.address}</p>
				<p>Rating: {restaurant.rating}</p>
				<p className='text-bg-danger del' onClick={() => handleDelete(restaurant.rest_id)}>DELETE</p>
			</div>
		)
	})
  	return (
    	<>
			<div>
			<h2>Restaurants</h2>
				<div className='restaurants_list'>
					{rest_list}
				</div>
			</div>
    	</>
  	)
}