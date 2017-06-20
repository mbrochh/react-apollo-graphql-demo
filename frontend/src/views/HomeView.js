import React from 'react'
import { Link } from 'react-router-dom'
import { gql, graphql } from 'react-apollo'

const query = gql`{
  allMessages {
    edges {
      node {
        id
        message
      }
    }
  }
}`

class HomeView extends React.Component {
  render() {
    let { data } = this.props
    if (data.loading) {
      return <div>Loading...</div>
    }
    return (
      <div>
        {data.allMessages.edges.map((item, index) => (
          <p key={item.node.id}>
            <Link to={`/messages/${item.node.id}/`}>
              {item.node.message}
            </Link>
          </p>
        ))}
      </div>
    )
  }
}

HomeView = graphql(query)(HomeView)

export default HomeView
