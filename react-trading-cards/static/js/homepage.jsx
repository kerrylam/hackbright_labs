class Homepage extends React.Component {
	render(){
		return (
            <div>
                <p>Hello! Check out my friends as trading cards.</p>
                <a href="/cards">Click here to see the trading cards.</a>
                <img src="/static/img/balloonicorn.jpg" />
            </div>
        );
	}
}

ReactDOM.render(<Homepage />, document.getElementById('app'));