"use client"

import { Navbar } from "@/components/navbar"
import StoryList from "@/components/story-list"
import { searchStories } from "@/lib/data"
import { useSearchParams } from "next/navigation"
import { useEffect, useState } from "react"

export default function SearchPage() {
  const searchParams = useSearchParams()
  const query = searchParams.get("q") || ""

  const [stories, setStories] = useState(null)

  useEffect(() => {
    searchStories(query).then(data => setStories(data))
  }, [query])

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-2">Search Results</h1>
        <p className="text-gray-600 mb-8">Showing results for: "{query}"</p>

        {stories === null ? (<div className="text-center py-12">
            <p className="text-xl text-gray-600">Loading...</p>
          </div>) : stories.length > 0 ? (
          <StoryList stories={stories} />
        ) : (
          <div className="text-center py-12">
            <p className="text-xl text-gray-600">No stories found matching your query.</p>
          </div>
        )}
      </div>
    </div>
  )
}
