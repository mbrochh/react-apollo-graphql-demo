import React from 'react'
import { gql, graphql } from 'react-apollo'

const mutation = gql`
mutation CreateView($message: String!) {
  createMessage(message: $message) {
    formErrors,
    message {
      id,
    }
  }
}
`

class CreateView extends React.Component {
  handleSubmit(e) {
    e.preventDefault()
    let formData = new FormData(this.form)
    this.props
      .mutate({ variables: { message: formData.get('message') } })
      .then(res => {
        window.location.replace(`/`)
      })
      .catch(err => {
        console.log('Network error!')
      })
  }

  render() {
    return (
      <div>
        <h1>Create</h1>
        <form
          ref={ref => (this.form = ref)}
          onSubmit={e => this.handleSubmit(e)}
        >
          <textarea name="message" />
          <button type="submit">Submit</button>
        </form>
      </div>
    )
  }
}
CreateView = graphql(mutation)(CreateView)
export default CreateView
