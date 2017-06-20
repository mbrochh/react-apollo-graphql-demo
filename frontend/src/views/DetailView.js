import React from 'react'
import { gql, graphql } from 'react-apollo'

const query = gql`
query DetailView($id: ID!) {
  message(id: $id) {
    id,
    message
    creationDate,
  }
}
`

class DetailView extends React.Component {
  render() {
    let { data } = this.props
    if (data.loading) {
      return <div>Loading...</div>
    }
    return (
      <div>
        <h1>Message: {data.message.id}</h1>
        <p>{data.message.creationDate}</p>
        <p>{data.message.message}</p>
      </div>
    )
  }
}

const queryOptions = {
  options: props => ({
    variables: {
      id: props.match.params.id,
    },
  }),
}
DetailView = graphql(query, queryOptions)(DetailView)
export default DetailView
