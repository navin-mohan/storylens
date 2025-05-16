"use client"

import StoryList from "@/components/story-list"
import { Navbar } from "@/components/navbar"
import { useEffect, useState } from "react"
import { getStories } from "@/lib/data"


export default function Home() {
  const [stories, setStories] = useState([])

  function fetchStories() {
    getStories().then(
      data => setStories(data)
    )
  }
  useEffect(fetchStories, [])
  return (
    <main className="min-h-screen bg-gray-50">
      <Navbar />
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-8">Featured Stories</h1>
        <StoryList stories={stories} />
      </div>
    </main>
  )
}
